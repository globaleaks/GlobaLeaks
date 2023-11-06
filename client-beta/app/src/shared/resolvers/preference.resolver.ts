import {Injectable} from "@angular/core";
import { Router } from "@angular/router";
import {Observable, of} from "rxjs";
import {HttpService} from "@app/shared/services/http.service";
import {preferenceResolverModel} from "@app/models/resolvers/preference-resolver-model";
import {AuthenticationService} from "@app/services/authentication.service";
import {map} from "rxjs/operators";

@Injectable({
  providedIn: "root"
})
export class PreferenceResolver  {
  dataModel: preferenceResolverModel = new preferenceResolverModel();

  constructor(private router: Router, private httpService: HttpService, private authenticationService: AuthenticationService) {
  }

  resolve(): Observable<boolean> {
    if (this.authenticationService.isSessionActive()) {
      return this.httpService.requestUserPreferenceResource().pipe(
        map((response: preferenceResolverModel) => {
          this.dataModel = response;
          if (this.dataModel.password_change_needed) {
            this.router.navigate(["/action/forcedpasswordchange"]).then();
          } else if (this.dataModel.require_two_factor) {
            this.router.navigate(["/action/forcedtwofactor"]).then();
          }
          return true;
        })
      );
    }
    return of(true);
  }
}
