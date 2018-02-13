import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {ReactiveFormsModule} from '@angular/forms';

import {AppComponent} from './app.component';
import {DynamicFormComponent} from './dynamic-form/dynamic-form.component';
import {Risks} from './providers/services/risks';
import {Api} from './providers/api';
import {AppRoutingModule} from './app-routing.module';
import {RouteReuseStrategy} from "@angular/router";
import {CustomRouteReuseStrategy} from "./route-reuse.strategy";


@NgModule({
  declarations: [
    AppComponent,
    DynamicFormComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [{
      provide: RouteReuseStrategy,
      useClass: CustomRouteReuseStrategy
    },Risks, Api, DynamicFormComponent],
  bootstrap: [AppComponent]
})
export class AppModule {
}
