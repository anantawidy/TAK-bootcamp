const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("Booking", function () {
  it("Create Booking", async function () {

    const response = await request_url
      .post("/booking")
      .set('Accept','application/json')
      .send({
        firstname: "Ananta",
        lastname: "Widyaswara",
        totalprice: 1000000,
        depositpaid: true,
        bookingdates: {
            checkin: "2023-02-01",
            checkout: "2023-02-05",
        }
      });

    assert(response.statusCode).to.eql(200);
    assert(response.body.booking.firstname).to.eql("Ananta");
    assert(response.body.booking.lastname).to.eql("Widyaswara");
    assert(response.body.booking.totalprice).to.eql(1000000);
    assert(response.body.booking.depositpaid).to.eql(true);
    assert(response.body.booking.bookingdates.checkin).to.eql("2023-02-01");
    assert(response.body.booking.bookingdates.checkout).to.eql("2023-02-05");

  })

  it("GET Booking", async function () {

    const response = await request_url
      .get("/booking/1797")
      //booking id auto changes, please help to update booking id
      .set('Accept','application/json')
      .send();

    assert(response.statusCode).to.eql(200);
  })

  it("GET Booking IDs", async function () {

    const response = await request_url
      .get("/booking")
      .set('Accept','application/json')
      .send();

    assert(response.statusCode).to.eql(200);
  })
});