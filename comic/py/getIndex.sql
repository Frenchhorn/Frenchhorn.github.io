select
  comic.comicID,
  comic.name,
  comic.author,
  count(episode.vol),
  count(episode.episode),
  count(episode.special)
from
  episode
join
  comic
on
  episode.comic_id = comic.id
group by
  episode.comic_id
order by
  comic.comicID