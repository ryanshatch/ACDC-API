// Prepare the request body dynamically
pm.variables.set("requestBody", JSON.stringify({
    inmates: [
        { firstName: "Foster", lastName: "Fech" }
    ]
}));

// Optional: Log the request body for debugging
console.log("Request Body:", pm.variables.get("requestBody"));

// // Prepare the request body dynamically
// pm.variables.set("requestBody", JSON.stringify({
//     inmates: [
//         { firstName: "Foster", lastName: "Fech" }
//     ]
// }));

// // Optional: Log the request body for debugging
// console.log("Request Body:", pm.variables.get("requestBody"));

// // Ensure the status code is 200
// pm.test("Status Code is 200", function () {
//     pm.response.to.have.status(200);
// });

// // Check if the response contains the `found_inmates` property
// pm.test("Response has found_inmates data", function () {
//     const responseData = pm.response.json();
//     pm.expect(responseData).to.have.property("found_inmates");
//     pm.expect(responseData.found_inmates).to.be.an("array");
// });

// // Optional: Validate the first inmate's details
// pm.test("First inmate has correct details", function () {
//     const responseData = pm.response.json();
//     const firstInmate = responseData.found_inmates[0];
//     pm.expect(firstInmate).to.have.property("firstName", "Foster");
//     pm.expect(firstInmate).to.have.property("lastName", "Fech");
// });

// pm.variables.set("requestBody", JSON.stringify({
//     inmates: [
//         { firstName: "Foster", lastName: "Fech" }
//     ]
// }));

// // Optional: Log to Postman Console for debugging
// console.log("Request Body:", pm.variables.get("requestBody"));