-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	        FROM `states`
	       WHERE `name` = "California")
ORDER BY `id`;
