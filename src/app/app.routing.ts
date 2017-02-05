import { Routes, RouterModule } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';

// Import our components
// Component views import
import {HomeComponent} from './home/home.component';
import { TestComponent } from './test/test.component';
import { JournalComponent } from './journal/journal.component';
import { InsightsComponent } from './insights/insights.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent,
    children: [
      {path: 'journal', component: JournalComponent},
      {path: 'insights', component: InsightsComponent},
    ]
  },
  
  { path: 'test', component: TestComponent },


  // If route doesn't exist
  {path: '**', redirectTo: '', pathMatch: 'full'}
];
// Here we are exporting our routes
export const routing = RouterModule.forRoot(appRoutes);
// Here we are combining our routing components into a single array. We will use this a little later when we update our root module
export const routedComponents = [
  HomeComponent,
  TestComponent,
  InsightsComponent
];
