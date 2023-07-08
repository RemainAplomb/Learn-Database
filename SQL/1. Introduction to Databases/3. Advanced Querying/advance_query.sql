-- Data Definition Language (DDL)

-- Create
CREATE TABLE companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(100),
    address VARCHAR(200),
    industry VARCHAR(50)
);

-- Alter
ALTER TABLE companies
ADD contact_number VARCHAR(20);

-- Drop
DROP TABLE companies;

-- Data Control Language (DCL)

-- Grant
GRANT SELECT, INSERT ON companies TO user1;

-- Revoke
REVOKE SELECT, INSERT ON companies FROM user1;

-- Transaction Control Language (TCL)

-- Begin
BEGIN;

-- Commit
COMMIT;

-- Rollback
ROLLBACK;
