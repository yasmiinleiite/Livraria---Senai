import { inject } from "@angular/core";
import { CanActivateFn, Router } from "@angular/router";
import { AuthService } from "./services/auth.services";

export const authGuard: CanActivateFn = () => {
    const auth = inject(AuthService)
    const router = inject(Router)
    if (auth.isAuthenticated()) return true
    router.navigateByUrl('/login')
    return false
}