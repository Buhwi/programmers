-- 코드를 입력하세요
SELECT COUNT(user_id) as COUNT
FROM user_info
WHERE YEAR(JOINED) = 2021 AND age >= 20 AND age <= 29;