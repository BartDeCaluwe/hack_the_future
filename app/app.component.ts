import { Component } from '@angular/core';
import { SensorService } from './services/sensor.service'

@Component({
  moduleId: module.id,
  selector: 'my-app',
  templateUrl: './app.component.html',
  providers: [ SensorService ]
})
export class AppComponent  { }
