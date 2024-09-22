import {
    withAuthInfo,
    useRedirectFunctions,
    useLogoutFunction,
} from "@propelauth/react";

const PropelAuth = withAuthInfo((props) => {
    const logoutFunction = useLogoutFunction();
    const { redirectToLoginPage, redirectToSignupPage, redirectToAccountPage } =
        useRedirectFunctions();
    // Or if you want to make links instead
    // const { getLoginPageUrl, getSignupPageUrl, getAccountPageUrl } = useHostedPageUrls()

    if (props.isLoggedIn) {
        return (
            <div className="mt-5">
                <p className="text-xl">You are logged in as {props.user.email}</p>
                <button 
                    className="mt-5 mx-2 w-1/2 md:w-full transition ease-in-out hover:-translate-y-1 duration-300 border-4 border-tinderOrange p-2 px-8 md:text-lg rounded-xl"
                    onClick={() => redirectToAccountPage()}>Account</button>
                <button 
                    className="mt-5 mx-2 w-1/2 md:w-full transition ease-in-out hover:-translate-y-1 duration-300 border-4 border-tinderOrange p-2 px-8 md:text-lg rounded-xl"
                    onClick={() => logoutFunction(true)}>Logout</button>
            </div>
        );
    } else {
        return (
            <div>
                <p>You are not logged in</p>
                <button 
                    className="mt-5 mx-5 w-1/2 md:w-full transition ease-in-out hover:-translate-y-1 duration-300 border-4 border-tinderOrange p-2 px-8 md:text-lg rounded-xl"
                    onClick={() => redirectToLoginPage()}>Login</button>
                <button
                    className="mt-5 mx-5 w-1/2 md:w-full transition ease-in-out hover:-translate-y-1 duration-300 border-4 border-tinderOrange p-2 px-8 md:text-lg rounded-xl"
                    onClick={() => redirectToSignupPage()}>Signup</button>
            </div>
        );
    }
});

export default PropelAuth;
