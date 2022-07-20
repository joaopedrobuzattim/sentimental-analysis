CREATE table if not exists issues (
  id serial NOT NULL PRIMARY KEY,
  repositoryId integer NOT NULL REFERENCES main_repositories(id),
  issueNumber integer NOT NULL,
  issueId integer NOT null,
  userId integer NOT NULL,
  body text,
  type varchar(50) NOT NULL CHECK (type = 'issue'  or type = 'pull_request'),
  title text NOT NULL,
  creationDate timestamp NOT NULL,
  updateDate timestamp not null,
  createdAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updatedAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deletedAt timestamp
)