import { Injectable } from '@angular/core';
import { Http, Headers, URLSearchParams } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class SensorService {
    url = 'http://192.168.50.149:5000';

    constructor(private http: Http) {
        console.log('Sensor Service Initialized...');
    }

    // getTemperature() {
    //     return this.http.get('/api/temperature')
    //         .map(res => res.json());
    // }

    getButtonStatus() {
        var url = 'http://192.168.50.149:5000/getButtonState';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }

    getLightState() {
        var url = 'http://192.168.50.149:5000/getLightState';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }

    getSoundState() {
        var url = 'http://192.168.50.149:5000/getSoundState';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }

    getTemperatureState() {
        var url = 'http://192.168.50.149:5000/getTemperatureState';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }

    getDistanceState() {
        var url = 'http://192.168.50.149:5000/getUltrasoundDistanceState';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }

    // postDistanceState(data: any) {
    //     // {"team": {"id": 6}, "sensor": { "id": "1", "state": "true", "value": "1"}}
    //     var object: URLSearchParams;
    //     object.set('team', 'id: 6');
    //     var headers = new Headers();
    //     headers.append('Content-Type', 'application/x-www-form-urlencoded');
    //     return this.http.post('http://192.168.50.148:4000/api/', object, { headers })
    //         .map(res => res.json());
    // }
}