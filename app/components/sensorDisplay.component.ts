import { Component } from '@angular/core';
import { SensorService } from '../services/sensor.service'

@Component({
  moduleId: module.id,
  selector: 'pi',
  templateUrl: 'sensorDisplay.component.html',
})
export class SensorDisplayComponent {
  panic: any;
  light: any;
  sound: any;
  temperature: any;
  distance: any;

  constructor(private sensorService: SensorService) {
    this.getButtonState();
    this.getLichtState();
    this.getSoundState();
    this.getTemperatureState();
    this.getDistance();
    this.repeatCalls();
  }

  getButtonState() {
    this.sensorService.getButtonStatus()
      .subscribe(data => {
        console.log(data);
        this.panic = data;
      });
  }

  getLichtState() {
    this.sensorService.getLightState()
      .subscribe(data => {
        console.log(data);
        this.light = data;
      });
  }

  getSoundState() {
    this.sensorService.getSoundState()
      .subscribe(data => {
        console.log(data);
        this.sound = data;
      });
  }

  getTemperatureState() {
    this.sensorService.getTemperatureState()
      .subscribe(data => {
        console.log(data);
        this.temperature = data;
      });
  }

  getDistance() {
    this.sensorService.getDistanceState()
      .subscribe(data => {
        console.log(data);
        this.distance = data;
      });
  }

  repeatCalls() {
    setInterval(() => {
      this.getButtonState();
      this.getLichtState();
      this.getTemperatureState();
      this.getDistance();
      this.getSoundState();
    }, 3000);
  }
}
