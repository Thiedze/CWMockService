CREATE TABLE "mock-service".services (
	id int8 NOT NULL,
	"name" varchar(4096) NULL,
	httpmethod varchar(4096) NULL,
	httpurl varchar(4096) NULL,
	payload bytea NULL,
	"type" varchar NULL,
	httpstatus int4 NULL,
	mimetype varchar NULL,
	body text NULL,
	ignorerequestbody bool NULL,
	CONSTRAINT services_pkey PRIMARY KEY (id)
);