import { useState } from "react";
import { withAuthInfo, useAuthInfo } from "@propelauth/react";
import "../App.css";
import "../input.css";


const Main = withAuthInfo((props) => {
  const auth = useAuthInfo();

  const [name, setName] = useState(null);
  const [pfp, setPfp] = useState(null);
  const [email, setEmail] = useState(null);

  const [matched, setMatched] = useState(false);

  const mobileView = window.innerWidth < 768;

  function matchMe() {
    if (matched) {
      return;
    }

    console.log("Matching...");
    // Send a get request to https://pennapps-project.onrender.com/user/{props.user.email}
    // The response will be the email of a match
    fetch(`http://localhost:5001/user/${props.user.email}`)
      .then((response) => response.json())
      .then((data) => {
        console.log("Match data:", data);
        console.log("Match email:", data.closest_user);
        const matchEmail = data.closest_user;
        setEmail(matchEmail);
        console.log(matchEmail);
        console.log("setEmail");
  
        // Use matchEmail directly instead of waiting for state update
        fetch(`http://localhost:5001/user-info/${matchEmail}`)
          .then((response) => response.json())
          .then((data) => {
            setName(data.name);
            setPfp(data.profile_picture_url);
            console.log(pfp)
          })
          .catch((error) => {
            console.error("Error fetching match data:", error);
          });
      })
      .catch((error) => {
        console.error("Error fetching match email:", error);
      });
    // let match = auth.fetchUserMetadataByEmail(
    //     "sofiacegan@gmail.com",
    //     true // includeOrgs
    // );
    // console.log(match);

    // document.getElementById("matchProfile").querySelector("img").src =
    //     match.pictureUrl;

    const arrow = document.getElementById('arrow');
    arrow.classList.add('transition', 'duration-300', 'transform', 'md:-translate-y-0', 'translate-y-8', 'md:translate-x-16', 'ease-in-out');

    setTimeout(() => {

      // document.getElementById('reason').style.visibility = 'visible';
    }, 400);
    setMatched(true);
  }

  return (
    <div 
      id="main"
      className="h-full w-full"
      >
        <div 
          className="flex flex-col items-center justify-center h-full w-full">
          <div
            className="flex flex-col justify-center items-center mt-5"
          >
            <img 
              src='logo2.png'
              className="w-3/5"
            />
          
          </div>
          <div id='button'>
            <button 
              id='matchButton'
              className="transition ease-in-out hover:-translate-y-1 hover:scale-110 duration-300 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange p-2 px-4 mt-5 text-white text-xl"
              style={{height: '90px', width: '270px', fontSize: '2.7rem'}}
              onClick={matchMe}
              >Match Me!
            </button>
          </div>
          <div className="flex flex-col md:flex-row justify-center items-center mt-16" style={{display:'flex', flexDirection: mobileView ? 'column' : 'row'}}>
            <div 
              id="profile"
              className="mt-5 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange flex justify-center items-center">
              <div 
                id="userProfile"
                className="bg-white m-3 rounded-xl flex flex-col ">
                  <div 
                    id="profileImage" 
                    className="bg-grey w-80 h-80 px-0 pt-0 flex items-end">
                    <img src={props.user.pictureUrl} alt="profile" style={{ 
                        width: '100%', 
                        height: '100%', 
                        objectFit: 'cover' 
                      }}/>
                  </div>
                  <p className="text-3xl pb-1 p-2 pt-3">{props.user.firstName + " " + props.user.lastName}</p>
                  <div 
                    id="email"
                    className="p-2">
                    <h1 className="text-xl">Email: {props.user.email}</h1>
                  </div>
              </div>
            </div>
            <div id="arrow">
              <p className="text-7xl text-tinderOrange mx-16 transform md:-translate-x-8 rotate-90 md:rotate-0">
                &#10095;
              </p>
            </div>
            <div 
              id="matchProfile"
              className="mt-5 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange flex justify-center items-center"
              style={{visibility:matched ? 'visible': 'hidden'}}>
              <div 
                id="profile"
                className="bg-white m-3 rounded-xl flex flex-col ">
                  <div 
                    id="profileImage" 
                    className="bg-grey w-80 h-80 px-0 pt-0 flex items-end">
                    <img src={pfp} alt="profile" style={{ 
                        width: '100%', 
                        height: '100%', 
                        objectFit: 'cover' 
                      }} />
                  </div>
                  <p className="text-3xl pb-1 p-2 pt-3">{name}</p>
                  <div 
                    id="email"
                    className="p-2">
                    <h1 className="text-xl">Email: {email}</h1>
                  </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
})

export default Main;