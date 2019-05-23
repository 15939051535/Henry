
SELECT * FROM items where img_front != 'None', img_side != 'None', img_obverse != 'None'; 

SELECT * FROM items where status != '000';

SELECT * FROM items where img_front_local != 'None', img_side_local != 'None', img_obverse_local != 'None';

SELECT * FROM items ORDER BY good_id LIMIT 20 OFFSET 0 * 20;

SELECT * FROM items where status != "000" and  1=1 order by good_id LIMIT 20 OFFSET 0 * 20;

select * from items where status like '%1';

update items set img_front = 'None', img_side = 'None', img_obverse = 'None', status = '000', img_front_local = 'None', img_side_local = 'None', img_obverse_local = 'None' where good_id = 1;

select * from items where good_id = 1;

update items set status = '111' where good_id in (0, 1);

CREATE TABLE IF NOT EXISTS items_test(
                good_id INT(10) PRIMARY KEY NOT NULL, 
                good_name VARCHAR(50),
                good_upc VARCHAR(20) NOT NULL,
                good_first VARCHAR(20),
                good_second VARCHAR(20),
                good_third VARCHAR(20),
                good_desc VARCHAR(50),
                good_price VARCHAR(20),
                good_p VARCHAR(20),
                good_c VARCHAR(20),
                good_x VARCHAR(20),
                img_front VARCHAR(200),
                img_side VARCHAR(200),
                img_obverse VARCHAR(200),
                create_time VARCHAR(20),
                status VARCHAR(3),
                img_front_local VARCHAR(100),
                img_side_local VARCHAR(100),
                img_obverse_local VARCHAR(100),
                good_imgs VARCHAR(2000)
            );
            
INSERT INTO items_test SELECT * FROM items;

select count(*) from items_test;

select count(*) from items_test where status = '000';

update items_test set status = '100' where good_id in (0,1);

update items_test set status = '010' where good_id in (2,3,4);

update items_test set status = '001' where good_id in (5,6,7,8);

update items_test set status = '110' where good_id in (9);

update items_test set status = '101' where good_id in (10,11);

update items_test set status = '011' where good_id in (12,13,14);

update items_test set status = '111' where good_id in (15,16);


select * from items_test where status <> '000' order by good_id;

select * from items_test where status like '1__' order by good_id;

select * from items_test where status like '__1' order by good_id;

select * from items_test where status like '_1_' order by good_id;

select * from items where status <> '000';

update items set status = '000' where good_id in(0, 1);


