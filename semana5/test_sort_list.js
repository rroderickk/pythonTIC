/**
 * ? A self-invoking function that finds the max
 * @number in an array.
 * */
(function find_max(nums) {
	let max_num = Number.NEGATIVE_INFINITY;

	for (let num of nums) {
		if (num > max_num) max_num = num
	}

	console.log(max_num);
})([1, 2, 3, 4, 5, 5, 40, 2000]) //! <-- This is the call to the function.