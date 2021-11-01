SELECT * FROM t_dept WHERE deptno = 30; 
SELECT ename 姓名, empno 编号, deptno 部门编号 FROM t_employees WHERE
job = '经理';
SELECT * FROM t_employees WHERE comm > sal;
SELECT * FROM t_employees WHERE comm > sal*0.6;
SELECT t_dept.*, t_employees.* FROM t_dept JOIN t_employees ON  t_employees.deptno = t_dept.deptno WHERE t_employees.deptno = 10 AND t_employees.job = '经理' OR t_employees.deptno = 20 AND t_employees.job = '分析员';
SELECT t_dept.*, t_employees.* 
FROM t_dept JOIN t_employees ON  t_employees.deptno = t_dept.deptno 
WHERE t_employees.deptno = 10 AND t_employees.job = '经理' OR t_employees.deptno = 20 AND t_employees.job = '分析员' OR t_employees.sal >= 3000 AND t_employees.job NOT IN ('经理', '武装上将');
SELECT * FROM t_employees WHERE comm IS NULL OR comm <1000;
SELECT * FROM t_employees WHERE CHAR_LENGTH(ename) = 3 ;
SELECT * FROM t_employees WHERE YEAR(hiredate) > 2000;
SELECT t_dept.*, t_employees.* 
FROM t_dept JOIN t_employees ON  t_employees.deptno = t_dept.deptno 
ORDER BY t_employees.empno
SELECT t_dept.*, t_employees.* 
FROM t_dept JOIN t_employees ON  t_employees.deptno = t_dept.deptno 
ORDER BY t_employees.sal DESC, t_employees.hiredate;
SELECT t_dept.dname, AVG(t_employees.sal) FROM t_employees JOIN t_dept ON t_employees.deptno = t_dept.deptno GROUP BY t_employees.deptno;
SELECT t_dept.dname, COUNT(*) FROM t_employees JOIN t_dept ON t_employees.deptno = t_dept.deptno GROUP BY t_employees.deptno;
SELECT t_employees.job, MAX(t_employees.sal), MIN(t_employees.sal), COUNT(*) FROM t_employees JOIN t_dept ON t_employees.deptno = t_dept.deptno GROUP BY t_employees.job;
