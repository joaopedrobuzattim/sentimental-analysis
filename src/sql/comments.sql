CREATE table if not exists comments (
  id serial NOT NULL PRIMARY KEY,
  commentId integer NOT NULL,
  userId integer NOT NULL,
  issueId integer REFERENCES issues(id) ON DELETE cascade not NULL,
  body text NOT NULL,
  creationDate timestamp NOT NULL,
  updateDate timestamp not null,
  createdAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updatedAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deletedAt timestamp
)