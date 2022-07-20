CREATE table if not exists most_stars_repositories (
  id serial NOT NULL PRIMARY KEY,
  owner varchar(100) NOT NULL,
  name varchar(100) NOT NULL,
  repositoryId integer NOT NULL,
  stars integer NOT NULL,
  forks integer NOT NULL,
  openIssues integer NOT NULL,
  creationDate timestamp not null,
  updateDate timestamp not null,
  createdAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updatedAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deletedAt timestamp
)