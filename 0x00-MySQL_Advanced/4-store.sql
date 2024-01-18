-- Create a trigger 

-- decrease quantity after order
DELIMITER $$
CREATE TRIGGER
decrese_items_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  DECLARE uQuantity INT; 

  SELECT quantity INTO uQuantity
  FROM items 
  WHERE items.name = NEW.item_name;

  SET uQuantity = uQuantity - NEW.number;

  UPDATE items SET quantity = uQuantity 
  WHERE items.name = NEW.item_name;
END$$
