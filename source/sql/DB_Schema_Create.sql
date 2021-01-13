CREATE TABLE "EXPECTANCY_TABLE" (
	"ID"	INTEGER,
	"COUNTRY"	TEXT,
	"YEAR"	INTEGER,
	"STATUS"	TEXT,
	"EXPECTANCY"	REAL,
	"MORTALITY"	REAL,
	"INFANT_DEATH"	REAL,
	"ALCOHOL"	REAL,
	"EXPENDITURE_PERCENT"	REAL,
	"HEPATITUS_B"	REAL,
	"MEASLES"	REAL,
	"BMI"	REAL,
	"UNDER_FIVE_DEATH"	REAL,
	"POLIIO"	REAL,
	"EXPENDITURE_TOTAL"	REAL,
	"DIPHTHERIA"	REAL,
	"HIV_AIDS"	REAL,
	"GDP"	REAL,
	"POPULATION"	REAL,
	"THIN_1TO19_YR"	REAL,
	"THIN_5TO9_YR"	REAL,
	"INC_COMPOSITION"	REAL,
	"SCHOOLING"	REAL,
	PRIMARY KEY("ID")
);

/* Source data location
https://www.kaggle.com/kumarajarshi/life-expectancy-who?select=Life+Expectancy+Data.csv
*/

CREATE TABLE "HAPPINESS_TABLE" (
	"ID"	INTEGER,
	"COUNTRY"	TEXT,
	"REGION"	TEXT,
	"HAPPINESS_RANK"	INTEGER,
	"HAPPINESS_SCORE"	REAL,
	"STANDARD_ERROR"	REAL,
	"ECONOMY"	REAL,
	"FAMILY"	REAL,
	"HEALTH"	REAL,
	"FREEDOM"	REAL,
	"TRUST"	REAL,
	"GENEROSITY"	REAL,
	"DYSTOPIA"	REAL,
	PRIMARY KEY("ID")
);

/* Source data location
https://www.kaggle.com/unsdsn/world-happiness?select=2015.csv
*/


/* 
View creation which Inner Join on Country Name between Happiness_2015_Table and Life_Expectancy_Table where Year of Life Expectancy is 2015
*/

CREATE VIEW EXPECT_HAPPINESS_VW AS
    SELECT E.ID AS E_ID,
           E.COUNTRY,
           E.YEAR,
           E.STATUS,
           E.EXPECTANCY,
           E.MORTALITY,
           E.INFANT_DEATH,
           E.ALCOHOL,
           E.EXPENDITURE_PERCENT,
           E.HEPATITUS_B,
           E.MEASLES,
           E.BMI,
           E.UNDER_FIVE_DEATH,
           E.POLIIO,
           E.EXPENDITURE_TOTAL,
           E.DIPHTHERIA,
           E.HIV_AIDS,
           E.GDP,
           E.POPULATION,
           E.THIN_1TO19_YR,
           E.THIN_5TO9_YR,
           E.INC_COMPOSITION,
           E.SCHOOLING,
           H.ID AS H_ID,
           H.COUNTRY,
           H.REGION,
           H.HAPPINESS_RANK,
           H.HAPPINESS_SCORE,
           H.STANDARD_ERROR,
           H.ECONOMY,
           H.FAMILY,
           H.HEALTH,
           H.FREEDOM,
           H.TRUST,
           H.GENEROSITY,
           H.DYSTOPIA
      FROM EXPECTANCY_TABLE E
           INNER JOIN
           HAPPINESS_TABLE H ON UPPER(H.Country) = UPPER(E.Country) 
     WHERE E.YEAR = '2015';
