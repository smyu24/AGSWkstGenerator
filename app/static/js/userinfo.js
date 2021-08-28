function separate() {
	let value = document.getElementById("data").innerHTML;
	let myArr = value.split(',');
	myArr[1] = myArr[1]. slice(2, -1);
	myArr[6] = myArr[6]. slice(2, -2);
	let final = "Welcome " + myArr[1] + " " + myArr[6] + "!"
	document.getElementById("username").innerHTML =  final;
}

function studentopt() {

}