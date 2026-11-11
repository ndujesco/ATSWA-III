#!/bin/sh
# Assembles src/* into index.html. Chapter content and past papers stay as
# separate files under data/ and are fetched on demand, so deploy the folder.
set -e
cd "$(dirname "$0")"

{
  cat <<'HEAD'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ATSWA Part III — The Great Lock-in</title>
<meta name="description" content="Your ATSWA Part III study desk: 62 chapters across Cost Accounting, Auditing, Taxation and Management, with worked examples, chapter quizzes and 3,360 past questions from 60 INSIGHT papers.">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F5F4EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#12110F" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23204E3C'/%3E%3Cpath d='M16 9C13 7 9 7 6 8v16c4-1 7 0 10 2 3-2 6-3 10-2V8c-3-1-7-1-10 1Zm0 0v17' fill='none' stroke='%23FCFBF7' stroke-width='1.6' stroke-linejoin='round'/%3E%3C/svg%3E">
</head>
<body>
HEAD
  cat src/page.html
  echo '<script>'
  cat src/subjects.js src/math.js src/render.js src/app.js src/quiz.js src/revision.js src/exams.js
  echo '</script>'
  echo '</body>'
  echo '</html>'
} > index.html

echo "built index.html  $(wc -c < index.html | tr -d ' ') bytes"
for f in data/*.js; do
  [ -e "$f" ] && echo "      $f  $(wc -c < "$f" | tr -d ' ') bytes"
done
