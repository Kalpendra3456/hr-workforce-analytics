# Database Relationships

## Overview

This document describes the relationships between the database tables used in the HR Workforce Analytics project. These relationships ensure data consistency, reduce redundancy, and enable comprehensive workforce analysis through SQL queries and Power BI dashboards.

---

# Relationship Summary

| Parent Table | Child Table | Relationship | Foreign Key |
|--------------|-------------|--------------|-------------|
| departments | employees | One-to-Many | department_id |
| jobs | employees | One-to-Many | job_id |
| locations | employees | One-to-Many | location_id |
| employees | attendance | One-to-Many | employee_id |
| employees | performance | One-to-Many | employee_id |
| employees | training | One-to-Many | employee_id |
| employees | recruitment | One-to-One* | employee_id |

> *Depending on the business process, recruitment may also be modeled as a One-to-Many relationship if multiple recruitment records are retained.

---

# Relationship Details

## 1. Departments → Employees

### Relationship Type
One-to-Many (1:N)

### Description

Each department can have multiple employees, while each employee belongs to only one department.

### Business Purpose

- Department headcount
- Workforce distribution
- Department salary analysis
- Department attrition analysis

---

## 2. Jobs → Employees

### Relationship Type

One-to-Many (1:N)

### Description

Each job role can be assigned to many employees.

### Business Purpose

- Job role distribution
- Salary comparison by role
- Performance by designation

---

## 3. Locations → Employees

### Relationship Type

One-to-Many (1:N)

### Description

Each office location may have multiple employees.

### Business Purpose

- Workforce by location
- Regional hiring
- Regional attrition
- Office capacity planning

---

## 4. Employees → Attendance

### Relationship Type

One-to-Many (1:N)

### Description

An employee can have multiple attendance records over time.

### Business Purpose

- Attendance tracking
- Leave analysis
- Absenteeism monitoring

---

## 5. Employees → Performance

### Relationship Type

One-to-Many (1:N)

### Description

Each employee can receive multiple performance evaluations during their employment.

### Business Purpose

- Performance trends
- Employee appraisal history
- Department performance analysis

---

## 6. Employees → Training

### Relationship Type

One-to-Many (1:N)

### Description

Employees can complete multiple training programs.

### Business Purpose

- Training completion
- Learning hours
- Certification tracking
- Skill development

---

## 7. Employees → Recruitment

### Relationship Type

One-to-One (1:1)

### Description

Each employee originates from a recruitment process represented by a recruitment record.

### Business Purpose

- Recruitment source analysis
- Hiring trends
- Time-to-hire analysis

---

# Entity Relationship Overview

```text
                 Departments
                      │
                      │
              department_id
                      │
                      ▼
                 Employees
        ┌─────────┼──────────┬──────────┐
        │         │          │          │
        ▼         ▼          ▼          ▼
      Jobs   Attendance  Performance Training
        │
        │
        ▼
   Recruitment

        ▲
        │
   Locations
```

---

# Foreign Key Reference

| Table | Foreign Key | References |
|---------|-------------|------------|
| employees | department_id | departments.department_id |
| employees | job_id | jobs.job_id |
| employees | location_id | locations.location_id |
| attendance | employee_id | employees.employee_id |
| performance | employee_id | employees.employee_id |
| training | employee_id | employees.employee_id |
| recruitment | employee_id | employees.employee_id |

---

# Why These Relationships Matter

The relationships allow analysts to:

- Join employee data with department information
- Compare salaries across job roles
- Analyze attendance by department
- Measure performance trends over time
- Evaluate training effectiveness
- Study recruitment outcomes
- Build executive HR dashboards using integrated data

---

# Benefits

A well-defined relational structure provides:

- Improved data integrity
- Reduced data duplication
- Faster SQL joins
- Accurate KPI calculations
- Better Power BI performance
- Scalable database design
- Reliable business reporting

---

# Conclusion

The relational design forms the backbone of the HR Workforce Analytics database. By linking employees with departments, jobs, locations, attendance, performance, training, and recruitment data, the model supports comprehensive workforce analysis and enables informed, data-driven HR decisions.