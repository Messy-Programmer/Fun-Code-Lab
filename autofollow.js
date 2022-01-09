const onOtherAccount = true;

let parentDiv;
if (onOtherAccount) {
  parentDiv = document.querySelector(
    "body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div"
  );
} else {
  parentDiv = document.querySelector(
    "#react-root > section > main > div > div.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.HVWg4 > div > div"
  );
}
let usersDiv = parentDiv.children;
let index = 0;
let total = 0;

function follower(startFrom, endAt) {
  if (startFrom) index = startFrom;
  if (endAt) total = endAt;
  if (index >= usersDiv.length) {
    if (onOtherAccount) {
      document
        .querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
        .scrollTo(0, index * 75);
    } else {
      window.scrollTo(0, document.body.scrollHeight);
    }
    setTimeout(() => {
      usersDiv = parentDiv.children;
      console.log("Scrolling...");
      index++;
      follower();
    }, 5000);
  } else {
    let currentUser;
    if (onOtherAccount) {
      currentUser = usersDiv[index].children[0];
    } else {
      currentUser = usersDiv[index];
    }
    //when users loaded to second page then first two part marges to one
    let followButtonDiv = currentUser.children[2] ?? currentUser.children[1];
    const followButton = followButtonDiv.children[0];
    followButton.click();

    const userDetailsDiv = currentUser.children[1];
    let userName;
    try {
      userName = userDetailsDiv.children[1].children[0].innerText;
    } catch (e) {
      userName = "unknown";
    }
    console.log(index + ". followed " + userName);
    if (total - 1 > index) {
      setTimeout(() => {
        index++;
        follower();
      }, 6000);
    } else {
      console.log("completed");
    }
  }
}
