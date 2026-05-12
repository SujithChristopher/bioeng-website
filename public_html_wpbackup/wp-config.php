<?php
define( 'WP_CACHE', true );

/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'u742491609_cmcbioengg');

/** Database username */
define('DB_USER', 'u742491609_cmcbioengg');

/** Database password */
define('DB_PASSWORD', '^Pv3qS3Lw');

/** Database hostname */
define('DB_HOST', 'localhost');

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', 'bf350c718020dc888b52f69d4e902fc5f76501e1e086a7878f4b3c4abcc3672d');
define('SECURE_AUTH_KEY', 'bc747bfcf1551c665779a428480f3dfa0c5a4ada55934d83ecb81ce088d42776');
define('LOGGED_IN_KEY', '52d2dd9599ef8362930b844d03ff0a115ae4887bf930c7d69665911cef8d96af');
define('NONCE_KEY', 'dea5b4c471d772cfdfff46e8c7f15f798dd1df06076217c7f3d95048a8164a49');
define('AUTH_SALT', '670749cca471eec5f19e17a78355f982bc5e5a09b181d7b40f2dac06d86ba4ff');
define('SECURE_AUTH_SALT', 'aed7bb4368b0467b09c1197b61e02cdf24622254d9979e158c0d096789958d89');
define('LOGGED_IN_SALT', 'b29ea035470befc548eca7dcfd8b3fe80e7372dfcb0009461de69fbadac8b3f6');
define('NONCE_SALT', 'e0c7c7905690f6fcbd6d443937cdaac7a9c0d5100f8e1642881195ac46a45d95');

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'RLI_';
define('WP_CRON_LOCK_TIMEOUT', 120);
define('AUTOSAVE_INTERVAL', 300);
define('WP_POST_REVISIONS', 20);
define('EMPTY_TRASH_DAYS', 7);
define('WP_AUTO_UPDATE_CORE', true);

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
