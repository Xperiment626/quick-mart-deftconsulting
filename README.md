# Jerry's Quick Mart

Jerry's Quick Mart in Orlando, FL is having its grand opening in 3 days. His previously hired software team lost all their files, and Jerry needs a solution for his grand opening.

Jerry has hired you for a quick solution to his problem. For the day of the Grand Opening, he has put out marketing nothing that all transactions must be in cash.

## Functionalities

1. Select whether customer is a Rewards member or Regular customer
2. Add items to cart
3. Remove individual items from cart
4. Empty cart option
5. View cart (including totals)
6. Checkout and Print receipt
7. Cancel transaction
  
### *Inventory is passed into the app in a text file, with item information on each line. The receipt is printed as a .txt file, with the transaction number and date included in the file name. Inventory is updated after checkout to avoid customers buying items that are out of stock*

---

# Instructions

> I was told to not use any external libraries. However, I used the built in libraries/packages from PYTHON 3.x just to write files and work with dates.

</br>
</br>

> I uploaded the code to GitHub with no executable files. You will find it in the following link: [Quick Mart](https://github.com/Xperiment626/quick-mart-deftconsulting)

---

# Brief explanation and Assumptions

> I wrote the program with Python 3.x below this document you will find the usage of the program.

### The first assumption I had made is that if you need a quick solution for your problem then a good start is to write a console app. If the client want a GUI I will make it

### Continuing with the app, for the customer membership, I made a choosable option for it, you will find it at the very start of the app

### As you will evaluating my solution and abilities in terms of Object Oriented Design I created 3 classes (Cart, Customer and Item) and the 'main' file (Quick_mart)

### I know that the commons in OOP is to make getters and setters but I just worked with getters and other kind of methods mainly

### For the functionality of adding an item to cart I assumed that first you want to choose your item from the inventary and then input the quantity of product you want. After that, I make a copy from the original inventory in order to ***pre-update*** the inventory so the person using the app will not buy anything out of stock. The real inventory is updated when the checkout is finally confirmed

### For the functionality of removing an item from the cart, I had 2 ideas, after ask about it I made that function in the following way: firts the cart is shown to you, then you need to choose the number(#) of item you want to removed, finally it will decrease 1 by 1. If it reachs 0 it will be removed from the cart

### It was needed to have an empty cart option so for this I just the built in methods for List in python, so I just erase all the List of items from cart

### For the view cart functionality, I just print the Item List and do some calculations for the total that is required in the document, and that prints as well

### For cheackout and receipt printing functionality, I only use the python 'os' package to perform CRUD operations with files. The document says that all transactions will be in cash, so the first thing to have a good transaction is to check if the cash is greater than the invoice, if so, the function will start to perform some calculations (subtotal, taxes, total, items sold etc) will then return an array/list of data needed for inventory update, even with cash value verification, I still ask the seller/customer if they are sure to proceed with the transaction, if the response is 'yes', the app will write the receipt to a file in the 'transaction' folder

### Finally, we have the 'cancel transaction' functionality not really a big deal, just start from the beginning

---

# Program usage

## First, we need to open terminal in the root directory of the github folder you downloaded

> Make sure you have python 3.x or upper in your OS
</br>

## Then we need to move to the 'program' folder then execute the following code in terminal

> Make sure that 'transaction' folder is created in the 'program' root folder

    $ python quick_mart.py

### or

    $ python3 quick_mart.py

### *If you have any questions about the program feel free to ask me*

# Contact

* Personal e-mail: `inaki.manosalvas@gmail.com`
* Student e-mail: `inaki.manosalvas@udla.edu.ec`
* WhatsApp: [Direct msg to my chat from WhatsApp API](https://api.whatsapp.com/send/?phone=593989180423&text=Buen%20d%C3%ADa%20I%C3%B1aki,%20soy%20...&app_absent=0)