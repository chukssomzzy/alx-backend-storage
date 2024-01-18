-- Create a trigger 

-- decrease quantity after order 
CREATE TRIGGER
IF NOT EXISTS decrese_items_quantity
INSERT AFTER ON orders
FOR EACH ROWS
BEGIN
  DECLARE uQuantity INT; 

  SELECT quantity INTO uQuantity
  FROM items 
  WHERE items.name = NEW.name;

  SET uQuantity = uQuantity - NEW.number;

  UPDATE items SET quantity = uQuantity 
  WHERE items.name = NEW.name;
END
