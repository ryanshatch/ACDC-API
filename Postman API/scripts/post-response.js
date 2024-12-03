// Ensure the response status is 200
pm.test("Status Code is 200", function () {
    pm.response.to.have.status(200);
});

// Check if the response contains the `found_inmates` property
pm.test("Response has found_inmates data", function () {
    const responseData = pm.response.json();
    pm.expect(responseData).to.have.property("found_inmates");
    pm.expect(responseData.found_inmates).to.be.an("array");
});

// Validate the first inmate's details
pm.test("First inmate has correct details", function () {
    const responseData = pm.response.json();
    const firstInmate = responseData.found_inmates[0];
    pm.expect(firstInmate).to.have.property("firstName", "Foster");
    pm.expect(firstInmate).to.have.property("lastName", "Fech");
});

// Log the response to the Postman Console for debugging
console.log("Response Data:", pm.response.json());

var template = `
<style type="text/css">
    .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}
    .tftable th {font-size:18px;background-color:#87ceeb;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}
    .tftable tr {background-color:#ffffff;}
    .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}
    .tftable tr:hover {background-color:#e0ffff;}
</style>

<table class="tftable" border="1">
    <tr>
        <th>First Name</th>
        <th>Last Name</th>
    </tr>
    
    {{#each response.found_inmates}}
        <tr id=row_{{@key}}>
            <td>{{firstName}}</td>
            <td>{{lastName}}</td>
        </tr>
    {{/each}}
</table>
`;

function constructVisualizerPayload() {
    return {response: pm.response.json()};
}

pm.visualizer.set(template, constructVisualizerPayload());