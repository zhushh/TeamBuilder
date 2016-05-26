--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO postgres;

--
-- Name: teamBuilder_comment; Type: TABLE; Schema: public; Owner: dbuser
--

CREATE TABLE "teamBuilder_comment" (
    id integer NOT NULL,
    content character varying(50) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    marker_id integer
);


ALTER TABLE "teamBuilder_comment" OWNER TO dbuser;

--
-- Name: teamBuilder_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: dbuser
--

CREATE SEQUENCE "teamBuilder_comment_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_comment_id_seq" OWNER TO dbuser;

--
-- Name: teamBuilder_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbuser
--

ALTER SEQUENCE "teamBuilder_comment_id_seq" OWNED BY "teamBuilder_comment".id;


--
-- Name: teamBuilder_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "teamBuilder_profile" (
    id integer NOT NULL,
    realname character varying(20) NOT NULL,
    phone character varying(20) NOT NULL,
    school character varying(20) NOT NULL,
    major character varying(20) NOT NULL,
    description text NOT NULL,
    user_id integer NOT NULL,
    role character varying(20),
    grade character varying(20) NOT NULL,
    department character varying(20) NOT NULL,
    tags character varying(20)[]
);


ALTER TABLE "teamBuilder_profile" OWNER TO postgres;

--
-- Name: teamBuilder_profile_commentList; Type: TABLE; Schema: public; Owner: dbuser
--

CREATE TABLE "teamBuilder_profile_commentList" (
    id integer NOT NULL,
    profile_id integer NOT NULL,
    comment_id integer NOT NULL
);


ALTER TABLE "teamBuilder_profile_commentList" OWNER TO dbuser;

--
-- Name: teamBuilder_profile_commentList_id_seq; Type: SEQUENCE; Schema: public; Owner: dbuser
--

CREATE SEQUENCE "teamBuilder_profile_commentList_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_profile_commentList_id_seq" OWNER TO dbuser;

--
-- Name: teamBuilder_profile_commentList_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbuser
--

ALTER SEQUENCE "teamBuilder_profile_commentList_id_seq" OWNED BY "teamBuilder_profile_commentList".id;


--
-- Name: teamBuilder_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "teamBuilder_profile_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_profile_id_seq" OWNER TO postgres;

--
-- Name: teamBuilder_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "teamBuilder_profile_id_seq" OWNED BY "teamBuilder_profile".id;


--
-- Name: teamBuilder_project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "teamBuilder_project" (
    id integer NOT NULL,
    title character varying(20) NOT NULL,
    description text NOT NULL,
    publisher_id integer NOT NULL
);


ALTER TABLE "teamBuilder_project" OWNER TO postgres;

--
-- Name: teamBuilder_project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "teamBuilder_project_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_project_id_seq" OWNER TO postgres;

--
-- Name: teamBuilder_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "teamBuilder_project_id_seq" OWNED BY "teamBuilder_project".id;


--
-- Name: teamBuilder_restriction; Type: TABLE; Schema: public; Owner: dbuser
--

CREATE TABLE "teamBuilder_restriction" (
    id integer NOT NULL,
    school character varying(20) NOT NULL,
    department character varying(20) NOT NULL,
    major character varying(20) NOT NULL,
    min_num integer,
    max_num integer,
    CONSTRAINT "teamBuilder_restriction_max_num_check" CHECK ((max_num >= 0)),
    CONSTRAINT "teamBuilder_restriction_min_num_check" CHECK ((min_num >= 0))
);


ALTER TABLE "teamBuilder_restriction" OWNER TO dbuser;

--
-- Name: teamBuilder_restriction_id_seq; Type: SEQUENCE; Schema: public; Owner: dbuser
--

CREATE SEQUENCE "teamBuilder_restriction_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_restriction_id_seq" OWNER TO dbuser;

--
-- Name: teamBuilder_restriction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbuser
--

ALTER SEQUENCE "teamBuilder_restriction_id_seq" OWNED BY "teamBuilder_restriction".id;


--
-- Name: teamBuilder_team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "teamBuilder_team" (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    captain_id integer,
    tags character varying(20)[],
    is_confirmed boolean NOT NULL,
    project_id integer,
    description text NOT NULL
);


ALTER TABLE "teamBuilder_team" OWNER TO postgres;

--
-- Name: teamBuilder_team_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "teamBuilder_team_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_team_id_seq" OWNER TO postgres;

--
-- Name: teamBuilder_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "teamBuilder_team_id_seq" OWNED BY "teamBuilder_team".id;


--
-- Name: teamBuilder_team_memberList; Type: TABLE; Schema: public; Owner: dbuser
--

CREATE TABLE "teamBuilder_team_memberList" (
    id integer NOT NULL,
    team_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE "teamBuilder_team_memberList" OWNER TO dbuser;

--
-- Name: teamBuilder_team_memberList_id_seq; Type: SEQUENCE; Schema: public; Owner: dbuser
--

CREATE SEQUENCE "teamBuilder_team_memberList_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "teamBuilder_team_memberList_id_seq" OWNER TO dbuser;

--
-- Name: teamBuilder_team_memberList_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbuser
--

ALTER SEQUENCE "teamBuilder_team_memberList_id_seq" OWNED BY "teamBuilder_team_memberList".id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_comment" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_comment_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_profile" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_profile_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_profile_commentList" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_profile_commentList_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_project" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_project_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_restriction" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_restriction_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_team" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_team_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_team_memberList" ALTER COLUMN id SET DEFAULT nextval('"teamBuilder_team_memberList_id_seq"'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add profile	7	add_profile
20	Can change profile	7	change_profile
21	Can delete profile	7	delete_profile
22	Can add team	8	add_team
23	Can change team	8	change_team
24	Can delete team	8	delete_team
25	Can add project	9	add_project
26	Can change project	9	change_project
27	Can delete project	9	delete_project
28	Can add comment	10	add_comment
29	Can change comment	10	change_comment
30	Can delete comment	10	delete_comment
31	Can add restriction	11	add_restriction
32	Can change restriction	11	change_restriction
33	Can delete restriction	11	delete_restriction
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 33, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$24000$9ZW6GnSrlpd2$jpdWMx1S67kn6jyK8EaAA44ZjhI7TJR/R+pymd0p/IY=	2016-05-26 17:06:16+08	t	peter			sptzxbbb@gmail.com	t	t	2016-05-25 16:16:04+08
2	pbkdf2_sha256$24000$lK0XLhrvqaxE$1XFBGTV3BHeMva2oRg5q9E8diYpN764Pp37NLSrqXrY=	\N	f	user001				f	t	2016-05-25 16:17:32+08
9	pbkdf2_sha256$24000$36Eap7ip1bla$5Mi7RgXrD0mJMp6IkIGnrjSvgmyCyfySRJJBKpyfkNw=	\N	f	user007				f	t	2016-05-26 18:21:00+08
3	pbkdf2_sha256$24000$5uTtiYNPlFzA$ii86FmOd3n2GEQObfBrdOvL7zGMC8QvCoi7AIMrZqqk=	\N	f	user002				f	t	2016-05-25 16:17:43+08
4	pbkdf2_sha256$24000$whUQIor4AGjQ$ozxR2y6tBloXXWg8n6oC1B3siYKVjdWwoHCA0UADQ7s=	\N	f	user003				f	t	2016-05-25 16:17:55+08
5	pbkdf2_sha256$24000$Ks72qJR1or96$/mVVh5GY5FJjCSm0WVP1Qk3ZUz4lYyQAxwzZPsfnkzU=	\N	f	user004				f	t	2016-05-25 16:18:09+08
6	pbkdf2_sha256$24000$Rt0pacwo98Ly$MYiykkIZPVEU7H7rcVbe7rO49uhoCeMbNrC55dmpJwc=	\N	f	user005				f	t	2016-05-26 18:20:42+08
7	pbkdf2_sha256$24000$1EbtWgpDalLO$hgo9iLvGxaqpwStVginVFBTCVZjlLZvOnkOZM4+7KyI=	\N	f	user006				f	t	2016-05-26 18:20:49+08
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 9, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2016-05-25 16:17:32.821646+08	2	user001	1	Added.	4	1
2	2016-05-25 16:17:43.98168+08	3	user002	1	Added.	4	1
3	2016-05-25 16:17:55.958984+08	4	user003	1	Added.	4	1
4	2016-05-25 16:18:09.573128+08	5	user004	1	Added.	4	1
5	2016-05-25 16:19:11.964369+08	1	Team object	1	Added.	8	1
6	2016-05-25 16:19:19.025005+08	1	Team object	2	Changed tags.	8	1
7	2016-05-25 16:19:59.986512+08	1	Team object	2	Changed tags.	8	1
8	2016-05-25 16:22:35.448762+08	1	Team object	2	Changed captain.	8	1
9	2016-05-25 16:24:21.253044+08	1	Project object	1	Added.	9	1
10	2016-05-25 16:52:41.160601+08	1	Team object	2	Changed members.	8	1
11	2016-05-25 17:20:13.770053+08	2	team2	1	Added.	8	1
12	2016-05-25 17:20:23.414348+08	2	team002	2	Changed name.	8	1
13	2016-05-25 20:16:24.169182+08	2	team002	2	Changed project.	8	1
14	2016-05-25 20:17:25.817986+08	3	Project2	1	Added.	9	1
15	2016-05-25 20:17:43.454123+08	1	team001	2	Changed project.	8	1
16	2016-05-25 20:19:41.362833+08	2	team002	2	Changed project.	8	1
17	2016-05-25 20:46:07.076402+08	1	peter	2	Changed password.	4	1
18	2016-05-26 17:06:42.660686+08	1	Comment object	1	Added.	10	1
19	2016-05-26 17:07:17.62368+08	2	Comment object	1	Added.	10	1
20	2016-05-26 17:07:24.200076+08	3	Comment object	1	Added.	10	1
21	2016-05-26 17:49:23.15976+08	2	user001	2	Added profile "user001's Profile".	4	1
22	2016-05-26 18:13:26.060723+08	1	peter	2	Added profile "peter's Profile".	4	1
23	2016-05-26 18:15:37.562377+08	2	user001	2	Changed school, major, grade and description for profile "user001's Profile".	4	1
24	2016-05-26 18:20:42.599673+08	6	user005	1	Added.	4	1
25	2016-05-26 18:20:49.562026+08	7	user006	1	Added.	4	1
26	2016-05-26 18:20:52.451778+08	8	user	1	Added.	4	1
27	2016-05-26 18:21:00.618428+08	9	user007	1	Added.	4	1
28	2016-05-26 18:21:37.893643+08	3	team003	1	Added.	8	1
29	2016-05-26 18:26:12.014644+08	9	user007	2	Added profile "user007's Profile".	4	1
30	2016-05-26 18:27:19.937591+08	8	user	3		4	1
31	2016-05-26 19:13:42.890954+08	3	user002	2	Added profile "user002's Profile".	4	1
32	2016-05-26 19:13:57.422467+08	3	user002	2	Changed commentList for profile "user002's Profile".	4	1
33	2016-05-26 21:34:10.371497+08	4	user003	2	Added profile "user003's Profile".	4	1
34	2016-05-26 21:34:15.807859+08	5	user004	2	Added profile "user004's Profile".	4	1
35	2016-05-26 21:34:20.60503+08	6	user005	2	Added profile "user005's Profile".	4	1
36	2016-05-26 21:34:24.952969+08	7	user006	2	Added profile "user006's Profile".	4	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 36, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	teamBuilder	profile
8	teamBuilder	team
9	teamBuilder	project
10	teamBuilder	comment
11	teamBuilder	restriction
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 11, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2016-05-25 16:14:45.036067+08
2	auth	0001_initial	2016-05-25 16:14:45.169573+08
3	admin	0001_initial	2016-05-25 16:14:45.202242+08
4	admin	0002_logentry_remove_auto_add	2016-05-25 16:14:45.21502+08
5	contenttypes	0002_remove_content_type_name	2016-05-25 16:14:45.241111+08
6	auth	0002_alter_permission_name_max_length	2016-05-25 16:14:45.253567+08
7	auth	0003_alter_user_email_max_length	2016-05-25 16:14:45.267327+08
8	auth	0004_alter_user_username_opts	2016-05-25 16:14:45.278564+08
9	auth	0005_alter_user_last_login_null	2016-05-25 16:14:45.308164+08
10	auth	0006_require_contenttypes_0002	2016-05-25 16:14:45.311564+08
11	auth	0007_alter_validators_add_error_messages	2016-05-25 16:14:45.320879+08
12	sessions	0001_initial	2016-05-25 16:14:45.342113+08
13	teamBuilder	0001_initial	2016-05-25 16:14:45.384965+08
14	teamBuilder	0002_team_tags	2016-05-25 16:14:45.40275+08
15	teamBuilder	0003_auto_20160525_0823	2016-05-25 16:23:58.350688+08
16	teamBuilder	0004_team_is_accepted	2016-05-25 16:25:38.085021+08
17	teamBuilder	0005_auto_20160525_0851	2016-05-25 16:51:17.249734+08
18	teamBuilder	0006_team_members	2016-05-25 16:52:25.861055+08
19	teamBuilder	0007_auto_20160525_0923	2016-05-25 17:23:21.735647+08
20	teamBuilder	0008_remove_profile_tags	2016-05-25 17:30:05.145163+08
21	teamBuilder	0009_auto_20160525_1216	2016-05-25 20:16:09.828182+08
22	teamBuilder	0010_auto_20160525_1217	2016-05-25 20:17:22.470719+08
23	teamBuilder	0011_auto_20160526_0905	2016-05-26 17:05:50.558728+08
24	teamBuilder	0012_auto_20160526_0942	2016-05-26 17:42:59.259914+08
25	teamBuilder	0013_auto_20160526_1119	2016-05-26 19:19:09.086225+08
26	teamBuilder	0014_auto_20160526_1333	2016-05-26 21:33:21.489186+08
27	teamBuilder	0015_auto_20160526_1407	2016-05-26 22:07:27.85443+08
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 27, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
w8z6ilnpxiziimnunxyku3rl3kvjq2fn	ZGViNWFkY2JhYWNlMWYwZWZkNGM1NGM3MmViMTZkNzMzZWU5MDBkODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NDdmM2VjYzJlY2NiY2NmMTQ1YjY0M2Y0MWFkMTE1OGVmOWNjNDZkIn0=	2016-06-08 16:16:39.696377+08
zfrszc7limhtx3pdnpz5oheuasiios6d	NDZjYzA2NzExZTBhOGU3MWJhMDA3MzE3MzUzNzNmOTYyZjIwNjAxODp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ3OWFhNTU0N2E5YTExMmU0M2YyZDA3NTJkZGQ3MTdmNWEwZTIxNTkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2016-06-08 20:46:07.081788+08
410ifqs3nr188lajuzkrp35dtxa2uotz	MDdkMzhkZjFhYzA4OTg2ZDRmMTY0ZDFmZGMwMDNhZTAxMTIzY2QyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDc5YWE1NTQ3YTlhMTEyZTQzZjJkMDc1MmRkZDcxN2Y1YTBlMjE1OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2016-06-09 17:06:16.318341+08
\.


--
-- Data for Name: teamBuilder_comment; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY "teamBuilder_comment" (id, content, "time", marker_id) FROM stdin;
1	This is a comment	2016-05-26 17:06:40+08	2
2	This is a comment	2016-05-26 17:06:50+08	3
3	This is a comment	2016-05-26 17:07:23+08	4
\.


--
-- Name: teamBuilder_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('"teamBuilder_comment_id_seq"', 3, true);


--
-- Data for Name: teamBuilder_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "teamBuilder_profile" (id, realname, phone, school, major, description, user_id, role, grade, department, tags) FROM stdin;
2	Peter	123	A	B	D	1	common	C		\N
1	张三	123456	A	B	D	2	common	C		\N
3					F	9	common			\N
4					This is a description	3	common			\N
5					This is a description	4	common			{}
6					This is a description	5	common			{}
7					This is a description	6	common			{}
8					This is a description	7	common			{}
\.


--
-- Data for Name: teamBuilder_profile_commentList; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY "teamBuilder_profile_commentList" (id, profile_id, comment_id) FROM stdin;
1	3	1
2	4	1
\.


--
-- Name: teamBuilder_profile_commentList_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('"teamBuilder_profile_commentList_id_seq"', 2, true);


--
-- Name: teamBuilder_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"teamBuilder_profile_id_seq"', 8, true);


--
-- Data for Name: teamBuilder_project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "teamBuilder_project" (id, title, description, publisher_id) FROM stdin;
1	Project1	This is project1	1
3	Project2	this is project2	1
\.


--
-- Name: teamBuilder_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"teamBuilder_project_id_seq"', 3, true);


--
-- Data for Name: teamBuilder_restriction; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY "teamBuilder_restriction" (id, school, department, major, min_num, max_num) FROM stdin;
\.


--
-- Name: teamBuilder_restriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('"teamBuilder_restriction_id_seq"', 1, false);


--
-- Data for Name: teamBuilder_team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "teamBuilder_team" (id, name, captain_id, tags, is_confirmed, project_id, description) FROM stdin;
1	team001	2	{tag1,tag2,tag3}	f	1	This is a description
2	team002	3	{}	f	3	This is a description
3	team003	9	{}	f	1	This is a description
\.


--
-- Name: teamBuilder_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"teamBuilder_team_id_seq"', 3, true);


--
-- Data for Name: teamBuilder_team_memberList; Type: TABLE DATA; Schema: public; Owner: dbuser
--

COPY "teamBuilder_team_memberList" (id, team_id, user_id) FROM stdin;
1	3	5
2	3	6
3	3	7
\.


--
-- Name: teamBuilder_team_memberList_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbuser
--

SELECT pg_catalog.setval('"teamBuilder_team_memberList_id_seq"', 3, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: teamBuilder_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_comment"
    ADD CONSTRAINT "teamBuilder_comment_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_profile_commentList_pkey; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_profile_commentList"
    ADD CONSTRAINT "teamBuilder_profile_commentList_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_profile_commentList_profile_id_a364e636_uniq; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_profile_commentList"
    ADD CONSTRAINT "teamBuilder_profile_commentList_profile_id_a364e636_uniq" UNIQUE (profile_id, comment_id);


--
-- Name: teamBuilder_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_profile"
    ADD CONSTRAINT "teamBuilder_profile_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_profile"
    ADD CONSTRAINT "teamBuilder_profile_user_id_key" UNIQUE (user_id);


--
-- Name: teamBuilder_project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_project"
    ADD CONSTRAINT "teamBuilder_project_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_restriction_pkey; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_restriction"
    ADD CONSTRAINT "teamBuilder_restriction_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_team_captain_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_team"
    ADD CONSTRAINT "teamBuilder_team_captain_id_key" UNIQUE (captain_id);


--
-- Name: teamBuilder_team_memberList_pkey; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_team_memberList"
    ADD CONSTRAINT "teamBuilder_team_memberList_pkey" PRIMARY KEY (id);


--
-- Name: teamBuilder_team_memberList_team_id_7a6db36b_uniq; Type: CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_team_memberList"
    ADD CONSTRAINT "teamBuilder_team_memberList_team_id_7a6db36b_uniq" UNIQUE (team_id, user_id);


--
-- Name: teamBuilder_team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_team"
    ADD CONSTRAINT "teamBuilder_team_pkey" PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: teamBuilder_comment_945c7b03; Type: INDEX; Schema: public; Owner: dbuser
--

CREATE INDEX "teamBuilder_comment_945c7b03" ON "teamBuilder_comment" USING btree (marker_id);


--
-- Name: teamBuilder_profile_commentList_69b97d17; Type: INDEX; Schema: public; Owner: dbuser
--

CREATE INDEX "teamBuilder_profile_commentList_69b97d17" ON "teamBuilder_profile_commentList" USING btree (comment_id);


--
-- Name: teamBuilder_profile_commentList_83a0eb3f; Type: INDEX; Schema: public; Owner: dbuser
--

CREATE INDEX "teamBuilder_profile_commentList_83a0eb3f" ON "teamBuilder_profile_commentList" USING btree (profile_id);


--
-- Name: teamBuilder_team_b098ad43; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "teamBuilder_team_b098ad43" ON "teamBuilder_team" USING btree (project_id);


--
-- Name: teamBuilder_team_memberList_e8701ad4; Type: INDEX; Schema: public; Owner: dbuser
--

CREATE INDEX "teamBuilder_team_memberList_e8701ad4" ON "teamBuilder_team_memberList" USING btree (user_id);


--
-- Name: teamBuilder_team_memberList_f6a7ca40; Type: INDEX; Schema: public; Owner: dbuser
--

CREATE INDEX "teamBuilder_team_memberList_f6a7ca40" ON "teamBuilder_team_memberList" USING btree (team_id);


--
-- Name: auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_comment_marker_id_e0ccaada_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_comment"
    ADD CONSTRAINT "teamBuilder_comment_marker_id_e0ccaada_fk_auth_user_id" FOREIGN KEY (marker_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_profi_comment_id_3bce42bf_fk_teamBuilder_comment_id; Type: FK CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_profile_commentList"
    ADD CONSTRAINT "teamBuilder_profi_comment_id_3bce42bf_fk_teamBuilder_comment_id" FOREIGN KEY (comment_id) REFERENCES "teamBuilder_comment"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_profi_profile_id_d1a78446_fk_teamBuilder_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_profile_commentList"
    ADD CONSTRAINT "teamBuilder_profi_profile_id_d1a78446_fk_teamBuilder_profile_id" FOREIGN KEY (profile_id) REFERENCES "teamBuilder_profile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_profile_user_id_e939c523_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_profile"
    ADD CONSTRAINT "teamBuilder_profile_user_id_e939c523_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_project_publisher_id_10fdb76c_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_project"
    ADD CONSTRAINT "teamBuilder_project_publisher_id_10fdb76c_fk_auth_user_id" FOREIGN KEY (publisher_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_team_captain_id_69fba53d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_team"
    ADD CONSTRAINT "teamBuilder_team_captain_id_69fba53d_fk_auth_user_id" FOREIGN KEY (captain_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_team_memberList_user_id_7e189c8c_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_team_memberList"
    ADD CONSTRAINT "teamBuilder_team_memberList_user_id_7e189c8c_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_team_member_team_id_946adb88_fk_teamBuilder_team_id; Type: FK CONSTRAINT; Schema: public; Owner: dbuser
--

ALTER TABLE ONLY "teamBuilder_team_memberList"
    ADD CONSTRAINT "teamBuilder_team_member_team_id_946adb88_fk_teamBuilder_team_id" FOREIGN KEY (team_id) REFERENCES "teamBuilder_team"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: teamBuilder_team_project_id_c0109c4f_fk_teamBuilder_project_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "teamBuilder_team"
    ADD CONSTRAINT "teamBuilder_team_project_id_c0109c4f_fk_teamBuilder_project_id" FOREIGN KEY (project_id) REFERENCES "teamBuilder_project"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

