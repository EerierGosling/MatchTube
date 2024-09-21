import "../App.css";
import "../input.css";


export default function Layout() {
  return (
    <div 
      id="main"
      className="h-full w-full"
      >
        <div 
          className="flex flex-col items-center justify-center h-full w-full">
          <div
            className="flex flex-col justify-center items-center"
          >
            <img 
              src='logoyoutube.png'
              className="w-1/6"
            />
            <h1
              className="text-2xl"
            >Project Name
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
                className="text-7xl text-tinderPink mx-5">
                  &rarr;
                </p>
            </div>
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
          </div>
          <div 
            id='matchInfo'
            className='w-1/2 mt-10'>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
            
        </div>
    </div>
  );
}