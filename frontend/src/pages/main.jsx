import "../App.css";
import "../input.css";


export default function Layout() {

  setTimeout(() => {
    hide(document.getElementById('matchProfile'));
    hide(document.getElementById('reason'));

  }, 50);

  function hide(thing) {
    thing.style.visibility = 'hidden';
  }

  function matchMe() {
    const arrow = document.getElementById('arrow');
    arrow.classList.add('transition', 'duration-300', 'transform', 'translate-x-16', 'ease-in-out');

    setTimeout(() => {
      document.getElementById('matchProfile').style.visibility = 'visible';
      document.getElementById('reason').style.visibility = 'visible';
    }, 400);
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
              src='logoyoutube.png'
              className="w-52"
            />
            <h1
              className="text-2xl"
            >MatchTube
            </h1>
          </div>
          <div className="flex justify-center items-center">
            <div 
              id="profile"
              className="mt-5 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange flex justify-center items-center">
              <div 
                id="userProfile"
                className="bg-white m-3 rounded-xl flex flex-col ">
                  <div 
                    id="profileImage" 
                    className="bg-grey w-80 h-48 px-2 pt-6 flex items-end">
                    <p className="text-3xl pb-1">Name</p>
                  </div>
                  <div 
                    id="about"
                    className="p-2">
                    <h1 className="text-xl">Likes: </h1>
                    <h1 className="text-xl">Recently Watched: </h1>
                  </div>
              </div>
            </div>
            <div 
                id="arrow">
                <p
                className="text-7xl text-tinderOrange mx-16 transform -translate-x-8">
                 &#10097;
                </p>
            </div>
            <div 
              id="matchProfile"
              className="mt-5 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange flex justify-center items-center">
              <div 
                id="profile"
                className="bg-white m-3 rounded-xl flex flex-col ">
                  <div 
                    id="profileImage" 
                    className="bg-grey w-80 h-48 px-2 pt-6 flex items-end">
                    <p className="text-3xl pb-1">Name</p>
                  </div>
                  <div 
                    id="about"
                    className="p-2">
                    <h1 className="text-xl">Likes: </h1>
                    <h1 className="text-xl">Recently Watched: </h1>
                  </div>
              </div>
            </div>
          </div>
          <div id='button'>
            <button 
              id='matchButton'
              className="transition ease-in-out hover:-translate-y-1 hover:scale-110 duration-300 bg-gradient-to-r rounded-xl from-tinderPink via-tinderRed to-tinderOrange p-2 px-4 mt-5 text-white text-xl"
              onClick={matchMe}
              >Match Me!
            </button>
          </div>
          <div 
            id='matchInfo'
            className='w-1/2 mt-10'>
            <p id='reason' className="text-xl text-center">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
            
        </div>
    </div>
  );
}