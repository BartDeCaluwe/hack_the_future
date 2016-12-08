import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { SensorDisplayComponent } from './components/sensorDisplayComponents';

@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent, SensorDisplayComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
