
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# A Week with Kana
## CS110 Final Project  Fall, 2024

## Team Members

Rijaa Zaidi & Bianna Chen

***

## Project Description

A game where the player collects food from the map to feed their pet cat.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Moving Character
2. Randomly spawning food
3. Text that explains your objective
4. colliding with food deletes and internally updates score
5. You can pet the cat exactly once (sprite updates from a closed mouth to an open one)

### Classes

- << You should have a list of each of your classes with a description >>
- Kana: The player character, initializes character and includes move methods
- Food: Creates collectible items, intializes the item with image and random coordinates

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | press space bar      |textbox is deleted and kana and food sprites appear  |
|  2                   | press arrow keys   | kana moves 50 pixels in whatever direction you press      |
|  3                  | using arrow keys, collide with any food object(pizza, fried rice, lassi, cookie)   | food object kana collided with is removed from the screen     |
|  4                   | collide with and remove all food objects   | a new text box opens which also features images of tomo(cat) and kana      |
|  5                   | press return key   | tomo opens it's mouth (petting the cat)      |
etc...

