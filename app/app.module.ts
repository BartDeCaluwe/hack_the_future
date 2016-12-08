import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';

import { AppComponent }  from './app.component';
import { SensorDisplayComponent } from './components/sensorDisplay.component';

@NgModule({
  imports:      [ BrowserModule, HttpModule ],
  declarations: [ AppComponent, SensorDisplayComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
