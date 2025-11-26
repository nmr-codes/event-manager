import React from "react";
import Button from "../Button/Button";
import styles from "./Hero.module.css";

export default function Hero() {
  return (
    <section className={styles.hero}>
      <h1 className={styles.title}>Welcome to HexRace</h1>
      <p className={styles.subtitle}>
        Fast, strategic, and beautifully minimalistic puzzle game.
      </p>
      <Button className={styles.cta}>Start Playing</Button>
    </section>
  );
}
