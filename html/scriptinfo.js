// function sumval(x,y){
//     console.log("hhhhh")
//     s=x+y
//     return s
// }

// i=1
// j=2
// a=sumval(i,j)
// console.log(a)

//another method --> arrow function
// i=1
// j=2
// sumval=()=>{
//     console.log("nnnnnn")

// }
// sumval()

// s1=0
// s2=0
// x=1
// y=10
// naturalsum = (x,y)=>{
//     for(i=x;i<=y;i++){
//         s1+=i
//     }
//     return s1
// }
// sum1=naturalsum(x,y)
// console.log(sum1)
 
// function naturalsum1(x,y){
//     for(i=x;i<=y;i++){
//         s2+=i
//     }
//     return s2
// }
// sum2=naturalsum1(x,y)
// console.log(sum2)



// prime

// setinfo = ()=>{
//     console.log("hi")
//     document.getElementById("adata").innerHTML="hi"
//     document.querySelector("#adata").innerHTML=100
//     document.querySelector(".bdata").innerHTML=200
//     document.querySelector(".bdata").style.color="red"

// }

// Data = ()=>{
//    console.log(document.querySelector("#name").value)

// }

// arr=[1,2,3,4,5]
// console.log(arr[0])
// arr1=new Array()

// s=0
// for(i=0;i<=arr.length;i++){
//     s+=i
// }
// console.log(s)

// data=['pineapple',3,4,'orange']
// console.log(data[0])

// const d=['Apple','OranGe','PinEapple']
// let i=0;
// while(i<d.length){
//     let word=d[i];
//     let count=0;
//     let j=0;
//     while(j<word.length){
//         if(word[j]>='A'&& word[j]=='Z'){
//             count++;

//         }
//         j++;
//     }
//     console.log(word.toUpperCase(),count);
//     i++;
// }

// display the count of capital letters in each item
// fruits = ["Apple","ORanGe","GraPe","BANAnA"]
// for(i=0;i<fruits.length;i++){
//     count = 0
//     for(j=0;j<fruits[i].length;j++){
//         if(fruits[i][j]>='A'&& fruits[i][j]<='Z'){
//             count = count + 1
//         }
//     }
//     console.log(fruits[i] + ":" + count)
// }

// // Defining object
// let person = {
// 	first_name: 'Mukul',
// 	last_name: 'Latiyan',

// 	//method
// 	getFunction: function () {
// 		return (`The name of the person is 
// 		${person.first_name} ${person.last_name}`)
// 	}
	
// }
// console.log(person.getFunction());


function validate(){

    username=document.getElementById("username").value
    email=document.getElementById("email").value
    Password=document.getElementById("password").value
    confirmPassword=document.getElementById("confirm-password").value

    

    document.getElementById("name-error").innerHTML=""
    document.getElementById("email-error").innerHTML=""
    document.getElementById("password-error").innerHTML=""
    document.getElementById("confirmpassword-error").innerHTML=""

    // let username=document.getElementById("UsernameError").value
    // let email=document.getElementById("EmailError").value
    // let Password=document.getElementById("PasswordError").value
    // let confirmPassword=document.getElementById("ConfirmpasswordError").value

    isValid = true;
    
    if(username.length<3||username.length>25){
        document.getElementById("name-error").innerHTML="Username must be between 3 and 25 characters";
        isValid=false;
    }

    if (Password.length<8){
        document.getElementById("password-error").innerHTML="Paswword must be atleast 8 characters that include atleast 1 lowercase character,1 uppercase characters,1 number and 1 special character in(!@#)";
        isValid=false;
    }
    if(confirmPassword==""){
        document.getElementById("confirmpassword-error").innerHTML="please enter the password again";
        isValid=false;
    }
    else if(Password!=confirmPassword){
        document.getElementById("confirmpassword-error").innerHTML="password do not match";
        isValid=false;
    }
    return isValid;

}
