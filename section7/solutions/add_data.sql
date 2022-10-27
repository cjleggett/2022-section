-- Add people
INSERT INTO people (name, senior) VALUES ("Amia", TRUE);
INSERT INTO people (name, senior) VALUES ("Isabelle", TRUE);
INSERT INTO people (name, senior) VALUES ("Same", FALSE);
INSERT INTO people (name, senior) VALUES ("David", FALSE);
INSERT INTO people (name, senior) VALUES ("Connor", TRUE);
INSERT INTO people (name, senior) VALUES ("Kalos", TRUE);
INSERT INTO people (name, senior) VALUES ("Caroline", TRUE);
INSERT INTO people (name, senior) VALUES ("Rebecca", FALSE);
INSERT INTO people (name, senior) VALUES ("Sophie", FALSE);
INSERT INTO people (name, senior) VALUES ("Joe", FALSE);
INSERT INTO people (name, senior) VALUES ("Stuart", FALSE);

-- Add courses
INSERT INTO courses (code, title) VALUES ("CS50", "Introduction to Computer Science");
INSERT INTO courses (code, title) VALUES ("STAT 110", "Introduction to Probability");
INSERT INTO courses (code, title) VALUES ("CS51", "Abstraction and Design in Computation");

-- Add instructors
INSERT INTO instructors (person_id, course_id) VALUES (5, 1);
INSERT INTO instructors (person_id, course_id) VALUES (4, 1);
INSERT INTO instructors (person_id, course_id) VALUES (10, 2);
INSERT INTO instructors (person_id, course_id) VALUES (11, 3);

-- Add students
INSERT INTO students (person_id, course_id, score) VALUES (1, 1, 60);
INSERT INTO students (person_id, course_id, score) VALUES (3, 1, 55.4);
INSERT INTO students (person_id, course_id, score) VALUES (5, 1, 89.4);
INSERT INTO students (person_id, course_id, score) VALUES (6, 1, 50);
INSERT INTO students (person_id, course_id, score) VALUES (3, 2, 32);
INSERT INTO students (person_id, course_id, score) VALUES (6, 2, 96);
INSERT INTO students (person_id, course_id, score) VALUES (7, 2, 98.5);
INSERT INTO students (person_id, course_id, score) VALUES (8, 2, 44.3);
INSERT INTO students (person_id, course_id, score) VALUES (7, 3, 67.2);
INSERT INTO students (person_id, course_id, score) VALUES (8, 3, 85.6);
INSERT INTO students (person_id, course_id, score) VALUES (9, 3, 56.6);
INSERT INTO students (person_id, course_id, score) VALUES (1, 3, 82.7);
INSERT INTO students (person_id, course_id, score) VALUES (9, 2, 57.8);