create table if not exists reactions (
  id serial NOT NULL PRIMARY KEY,
  issueId integer UNIQUE REFERENCES issues(id) ON DELETE cascade,
  commentId integer UNIQUE REFERENCES comments(id) ON DELETE cascade,
  positive integer NOT null,
  negative integer NOT null,
  laugh integer NOT null,
  hooray integer NOT null,
  confused integer NOT null,
  heart integer NOT null,
  rocket integer NOT null,
  eyes integer NOT null,
  createdAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updatedAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deletedAt timestamp
)

