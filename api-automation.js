const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("Booking", function () {
  it("Success Create Booking", async function () {

    const response = await request_url
      .post("/booking")
      .set('Accept','application/json')
      .send({
        firstname: "Ananta",
        lastname: "Widyaswara",
        totalprice: 1000000,
        depositpaid: true,
        bookingdates: {
            checkin: 2023-02-01,
            checkout: 2023-02-05,
        }
      });

    assert(response.statusCode).to.eql(200);
  })

  it("Success GET Booking", async function () {

    const response = await request_url
      .get("/booking/347")
      .set('Accept','application/json')
      .send();

    assert(response.statusCode).to.eql(200);
  })

  it("Success GET Booking IDs", async function () {

    const response = await request_url
      .get("/booking")
      .set('Accept','application/json')
      .send();

    assert(response.statusCode).to.eql(200);
  })
});