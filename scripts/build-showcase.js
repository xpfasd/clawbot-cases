#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const casesDir = path.join(root, "cases");
const templatesDir = path.join(root, "templates");
const templatePath = path.join(root, "scripts", "showcase-template.html");
const outputPath = path.join(root, "index.html");

const readText = (filePath) => fs.readFileSync(filePath, "utf8");

const escapeHtml = (value) =>
  value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\"/g, "&quot;")
    .replace(/'/g, "&#39;");

const escapeAttr = (value) => escapeHtml(value).replace(/`/g, "&#96;");

function inlineMarkdown(text) {
  const placeholders = [];
  const token = (html) => {
    placeholders.push(html);
    return `\u0000${placeholders.length - 1}\u0000`;
  };

  let result = text;

  result = result.replace(/`([^`]+)`/g, (_, code) => token(`<code>${escapeHtml(code)}</code>`));
  result = result.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, url) => {
    const safeLabel = escapeHtml(label);
    const safeUrl = escapeAttr(url);
    return token(`<a href="${safeUrl}" target="_blank" rel="noopener">${safeLabel}</a>`);
  });
  result = result.replace(/\*\*([^*]+)\*\*/g, (_, bold) => token(`<strong>${escapeHtml(bold)}</strong>`));
  result = result.replace(/__([^_]+)__/g, (_, bold) => token(`<strong>${escapeHtml(bold)}</strong>`));
  result = result.replace(/\*([^*]+)\*/g, (_, italic) => token(`<em>${escapeHtml(italic)}</em>`));
  result = result.replace(/_([^_]+)_/g, (_, italic) => token(`<em>${escapeHtml(italic)}</em>`));

  result = escapeHtml(result);

  return result.replace(/\u0000(\d+)\u0000/g, (_, index) => placeholders[Number(index)]);
}

function markdownToHtml(markdown) {
  const lines = markdown.split(/\r?\n/);
  const html = [];
  let inCode = false;
  let codeLang = "";
  let codeBuffer = [];
  let listType = null;

  const closeList = () => {
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
  };

  const flushCode = () => {
    if (!inCode) return;
    const codeContent = escapeHtml(codeBuffer.join("\n"));
    const langClass = codeLang ? ` class="language-${escapeAttr(codeLang)}"` : "";
    html.push(`<pre><code${langClass}>${codeContent}</code></pre>`);
    codeBuffer = [];
    codeLang = "";
    inCode = false;
  };

  lines.forEach((line) => {
    const trimmed = line.trim();

    if (trimmed.startsWith("```")) {
      if (inCode) {
        flushCode();
      } else {
        closeList();
        inCode = true;
        codeLang = trimmed.replace(/```/, "").trim();
      }
      return;
    }

    if (inCode) {
      codeBuffer.push(line);
      return;
    }

    if (!trimmed) {
      closeList();
      return;
    }

    const headingMatch = trimmed.match(/^(#{1,6})\s+(.*)$/);
    if (headingMatch) {
      closeList();
      const level = headingMatch[1].length;
      html.push(`<h${level}>${inlineMarkdown(headingMatch[2])}</h${level}>`);
      return;
    }

    const ulMatch = trimmed.match(/^[-*+]\s+(.*)$/);
    if (ulMatch) {
      if (listType !== "ul") {
        closeList();
        listType = "ul";
        html.push("<ul>");
      }
      html.push(`<li>${inlineMarkdown(ulMatch[1])}</li>`);
      return;
    }

    const olMatch = trimmed.match(/^\d+\.\s+(.*)$/);
    if (olMatch) {
      if (listType !== "ol") {
        closeList();
        listType = "ol";
        html.push("<ol>");
      }
      html.push(`<li>${inlineMarkdown(olMatch[1])}</li>`);
      return;
    }

    closeList();
    html.push(`<p>${inlineMarkdown(trimmed)}</p>`);
  });

  if (inCode) {
    flushCode();
  }
  closeList();

  return html.join("\n");
}

function stripMarkdown(markdown) {
  return markdown
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/`[^`]+`/g, " ")
    .replace(/#+\s+/g, " ")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/__([^_]+)__/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/_([^_]+)_/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
}

function toPreview(text, maxLength = 160) {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 1).trimEnd() + "…";
}

function extractSection(markdown, heading) {
  const pattern = new RegExp(`^##\\s*${heading}\\s*\\n([\\s\\S]*?)(?=\\n##\\s|\\n#\\s|$)`, "m");
  const match = markdown.match(pattern);
  return match ? match[1].trim() : "";
}

function extractCaseSummary(markdown) {
  const headings = ["场景", "Scenario", "Overview", "简介", "Summary", "Purpose"];
  for (const heading of headings) {
    const section = extractSection(markdown, heading);
    if (section) {
      const cleaned = stripMarkdown(section);
      if (cleaned) return cleaned;
    }
  }

  const paragraphs = markdown.split(/\n\s*\n/);
  for (const paragraph of paragraphs) {
    const cleaned = stripMarkdown(paragraph);
    if (cleaned) return cleaned;
  }

  return "";
}

function extractTemplateSummary(parsed, title) {
  if (parsed && typeof parsed.description === "string" && parsed.description.trim()) {
    return parsed.description.trim();
  }
  if (parsed && typeof parsed.summary === "string" && parsed.summary.trim()) {
    return parsed.summary.trim();
  }
  if (parsed && typeof parsed.title === "string" && parsed.title.trim()) {
    return parsed.title.trim();
  }
  if (parsed && typeof parsed.name === "string" && parsed.name.trim()) {
    return parsed.name.trim();
  }
  if (title) {
    return `Configuration template for ${title}.`;
  }
  return "";
}

function getTitle(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  if (match) return match[1].trim();
  return fallback;
}

function listDirectories(dirPath) {
  return fs
    .readdirSync(dirPath, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name);
}

function slugify(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

function collectCases() {
  const categories = listDirectories(casesDir);
  const cases = [];

  categories.forEach((category) => {
    const categoryPath = path.join(casesDir, category);
    const files = fs
      .readdirSync(categoryPath)
      .filter((file) => file.endsWith(".md"));

    files.forEach((file) => {
      const fullPath = path.join(categoryPath, file);
      const markdown = readText(fullPath);
      const title = getTitle(markdown, path.basename(file, ".md"));
      const html = markdownToHtml(markdown);
      const summary = extractCaseSummary(markdown);
      const preview = toPreview(summary || stripMarkdown(markdown), 180);
      cases.push({
        id: `case-${slugify(category)}-${slugify(file)}`,
        title,
        category,
        preview,
        content: html,
        source: path.relative(root, fullPath),
      });
    });
  });

  return cases.sort((a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
}

function collectTemplates() {
  const categories = listDirectories(templatesDir);
  const templates = [];

  categories.forEach((category) => {
    const categoryPath = path.join(templatesDir, category);
    const files = fs
      .readdirSync(categoryPath)
      .filter((file) => file.endsWith(".json"));

    files.forEach((file) => {
      const fullPath = path.join(categoryPath, file);
      const raw = readText(fullPath);
      let parsed;
      let content;
      try {
        parsed = JSON.parse(raw);
        content = JSON.stringify(parsed, null, 2);
      } catch (error) {
        parsed = null;
        content = raw.trim();
      }

      const title = parsed && (parsed.name || parsed.title) ? (parsed.name || parsed.title) : path.basename(file, ".json");
      const summary = extractTemplateSummary(parsed, title);
      const previewSource = summary || content.replace(/\s+/g, " ");
      const preview = toPreview(previewSource, 180);

      templates.push({
        id: `template-${slugify(category)}-${slugify(file)}`,
        title,
        category,
        preview,
        content: escapeHtml(content),
        source: path.relative(root, fullPath),
      });
    });
  });

  return templates.sort((a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
}

function build() {
  const cases = collectCases();
  const templates = collectTemplates();
  const payload = {
    cases,
    templates,
    generatedAt: new Date().toISOString(),
  };

  const template = readText(templatePath);
  const dataJson = JSON.stringify(payload).replace(/<\//g, "<\\/");
  const output = template.replace("__DATA_JSON__", dataJson);

  fs.writeFileSync(outputPath, output, "utf8");

  console.log(`Generated ${outputPath} with ${cases.length} cases and ${templates.length} templates.`);
}

build();
