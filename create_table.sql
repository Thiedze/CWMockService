CREATE TABLE "mock-service".services
(
  id bigint NOT NULL,
  name character varying(4096),
  httpmethod character varying(4096),
  httpurl character varying(4096),
  payload text,
  type character varying,
  httpstatus integer,
  mimetype character varying,
  body text,
  CONSTRAINT services_pkey PRIMARY KEY (id)
)