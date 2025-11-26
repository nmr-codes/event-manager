import React from "react";
import Button from "../Button/Button";
import styles from "./Header.module.css";

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.wrapper}>
        <div className={styles.logo}>HexRace</div>
        <nav className={styles.nav}>
          <a href="/">Home</a>
          <a href="/game">Game</a>
          <a href="/leaderboard">Leaderboard</a>
        </nav>
        <Button>Play Now</Button>
      </div>
    </header>
  );
}
