export function normalize(value) {
  return String(value).normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
}
export function searchEntries(entries, query, chapter = '', kind = '') {
  const words = normalize(query).split(/\s+/).filter(Boolean);
  return entries.filter(e => (!chapter || e.chapter_slug === chapter) && (!kind || e.kind === kind))
    .map(e => {
      const title = normalize(e.title), tag = normalize(e.tag || '');
      const context = normalize(`${e.section_title || ''} ${e.chapter_title || ''} ${e.aliases || ''}`);
      const body = normalize(e.text);
      const haystack = `${tag} ${title} ${context} ${body}`;
      if (!words.every(word => haystack.includes(word))) return null;
      const score = words.reduce((sum, word) => sum + (tag === word ? 100 : 0) +
        (title.includes(word) ? 15 : 0) + (context.includes(word) ? 5 : 0) + (body.includes(word) ? 1 : 0), 0);
      return {entry:e, score};
    }).filter(Boolean).sort((a,b) => b.score-a.score || a.entry.order-b.entry.order).map(r => r.entry);
}
