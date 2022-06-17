var CoffeeMachine = function(power, capacity) {
    this.setWaterAmount = function(amount) {
        if (amount < 0) {
            throw new Error("Value has to be positive.");
        }
        if (amount > capacity) {
            throw new Error("You can't put more water, than " + capacity);
        }
        waterAmount = amount;
    };

    this.getWaterAmount = function() {
        return waterAmount;
    };

    this.getPower = function() {
        return power;
    };
};

var coffeeMachine = new CoffeeMachine(100, 500);
coffeeMachine.setWaterAmount(450);
console.log(coffeeMachine.getWaterAmount());



/*Javascript ECS6: builder object mvc coffeMachine with OOP */

class CoffeeMachine {
    constructor(power) {
        this._power = power;
        this._waterAmount = 0;
    }

    get power() {
        return this._power;
    }

    set waterAmount(value) {
       
        if (value < 0) throw new Error("Negative water");
        this._waterAmount = value;
    }

    get waterAmount() {
        return this._waterAmount;
    }

    run() {
        setTimeout(() => console.log('Coffee is ready!'), 
		this.getTimeToBoil()
	);
    }

    getTimeToBoil() {
        return this._waterAmount * WATER_HEAT_CAPACITY * 80 / this._power;
    }
}

const coffeeMachine = new CoffeeMachine(10000);
coffeeMachine.waterAmount = 200;
coffeeMachine.run();





/*Javascript ECS2021: builder object mvc coffeMachine with OOP */

var CoffeeMachine = function(power, capacity) {
    this.waterAmount = 0;
    this.power = power;
    this.capacity = capacity;
};
CoffeeMachine.prototype.getTimeToBoil = function() {
    return this.waterAmount * 4200 * 80 / this.power;
};
CoffeeMachine.prototype.run = function() {
    setTimeout(function() {
        console.log('Coffee is ready!');
    }, this.getTimeToBoil());
    console.log('Coffee is ready!');
};
CoffeeMachine.prototype.setWaterAmount = function(amount) {
    if (amount < 0) {
        throw new Error("Value has to be positive.");
    }
    if (
        amount > this.capacity
    ) {
        throw new Error("You can't put more water, than " + this.capacity);
    }
    this.waterAmount = amount;
};
CoffeeMachine.prototype.addWater = function(amount) {
    this.setWaterAmount(this.waterAmount + amount);
};
var coffeeMachine = new CoffeeMachine(100000, 400);
coffeeMachine.addWater(200);
coffeeMachine.addWater(100);
coffeeMachine.addWater(300); // You can't put more water, than 400
coffeeMachine.run();






/*Javascript ECS2022: builder object mvc coffeMachine with OOP */

//create a builder object
var builder = {
    //create a coffeeMachine object
    coffeeMachine: function(name, price, type) {
        var coffeeMachine = {};

        //add properties to the coffeeMachine object
        coffeeMachine.name = name
        coffeeMachine.price = price
        coffeeMachine.type = type

        //add methods to the coffeeMachine object
        coffeeMachine.getName = function() {
            return this.name;
        }

        coffeeMachine.getPrice = function() {
            return this.price;
        }

        coffeeMachine.getType = function() {
            return this.type;
        }

        //return the coffeeMachine object
        return coffeeMachine;
    }
}


//create a new coffeeMachine object using the builder object
var coffeeMachine = builder.coffeeMachine("Nespresso", "£100", "Capsule");

//display the coffeeMachine object properties and methods
console.log(coffeeMachine.getName());
console.log(coffeeMachine.getPrice());
console.log(coffeeMachine.getType());







/*Javascript ECS2030: builder object mvc coffeMachine with OOP */

var CoffeeMachine = function(power, capacity) {
    this.waterAmount = 0;
    this.power = power;
    this.capacity = capacity;
};
CoffeeMachine.prototype.WATER_HEAT_CAPACITY = 4200;
CoffeeMachine.prototype.getTimeToBoil = function() {
    return this.waterAmount * this.WATER_HEAT_CAPACITY * 80 / this.power;
};
CoffeeMachine.prototype.run = function() {
    setTimeout(function() {
        alert( 'Кофе готов!' );
    }, this.getTimeToBoil());
};
CoffeeMachine.prototype.setWaterAmount = function(amount) {
   
    if (amount < 0) {
        throw new Error("Значение должно быть положительным");
    }
    if (amount
        > this.capacity) {
        throw new Error("Нельзя залить воды больше, чем " + this.capacity);
    }

    this.
    waterAmount = amount;
};
CoffeeMachine.prototype.addWater = function(amount) {
    this.setWaterAmount(this.waterAmount + amount);
};


var coffeeMachine = new CoffeeMachine(100000, 400);
coffeeMachine.addWater(200);
coffeeMachine.addWater(100);
coffeeMachine.addWater(300); // Нельзя залить больше, чем 400
coffeeMachine.run();
