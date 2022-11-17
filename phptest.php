<?php
use PHPUnit\Framework\TestCase;
include 'config.php';

final class phptest extends TestCase
{
	public function test_one(): void
	{
		$this->assertTrue(PasswordIsValid("isotope", "1s0t0p3"));
	}
	public function test_two(): void
	{
		$this->assertFalse(PasswordIsValid("isotope", "2s0t0p3"));
	}
}
?>