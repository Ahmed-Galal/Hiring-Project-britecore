import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {DynamicFormComponent} from './dynamic-form/dynamic-form.component';

/**
 * here i implement routing rules
 */
const routes: Routes = [

  {path: '', component: DynamicFormComponent},
  {path: 'risk/:id', component: DynamicFormComponent},
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
