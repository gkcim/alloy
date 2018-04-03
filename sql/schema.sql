CREATE TABLE alo_user(
    id          BIGSERIAL       PRIMARY KEY,
    nickname    VARCHAR(32)     NOT NULL UNIQUE,
    realname    VARCHAR(32)     NOT NULL DEFAULT '',
    password    VARCHAR(64)     NOT NULL DEFAULT '',
    email       VARCHAR(64)     DEFAULT NULL UNIQUE,
    phone       VARCHAR(16)     DEFAULT NULL UNIQUE
);
