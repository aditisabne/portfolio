import ErrorBoundary from "../utils/ErrorBoundary";
import Scene from "./Scene";

const CharacterModel = () => {
  return (
    <ErrorBoundary fallback={<div className="character-fallback">WebGL unavailable</div>}>
      <Scene />
    </ErrorBoundary>
  );
};

export default CharacterModel;
