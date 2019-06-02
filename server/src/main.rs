extern crate actix_web;
use actix_web::{server, App, HttpRequest, Responder};

static mut STATUS: bool = false;

fn get_status(_req: &HttpRequest) -> impl Responder {
	unsafe {
    	format!("{}", STATUS)
	}
}

fn toggle_status(_req: &HttpRequest) -> impl Responder {
	unsafe {
		STATUS = !STATUS;
    	format!("{}", STATUS)
	}
}

fn main() {
    server::new(|| {
        App::new()
            .resource("/status", |r| r.f(get_status))
            .resource("/toggle", |r| r.f(toggle_status))
    })
    .bind("127.0.0.1:8000")
    .expect("Can not bind to port 8000")
    .run();
}
